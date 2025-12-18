import 'dart:convert';

import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class CustomDragTargetControl extends StatelessWidget {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final FletControlBackend backend;

  const CustomDragTargetControl({
    super.key,
    required this.parent,
    required this.control,
    required this.children,
    required this.backend,
  });

  @override
  Widget build(BuildContext context) {
    String title = control.attrString("title", "Drag Target Title")!;
    String group = control.attrString("group", "")!;

    // Get "content" child controls
    final contentCtrls =
        children.where((c) => c.name == "content" && c.isVisible);

    // Turn first "content" control into a Widget
    final Widget child = contentCtrls.isNotEmpty
        ? (createControl(
            control, // parent
            contentCtrls.first.id, // <- child control id (String)
            control.isDisabled, // <- parentDisabled (or false if you prefer)
          ))
        : Text(title);

    Widget myControl = DragTarget<String>(
      // Called when a draggable is hovered over this target to decide
      // whether it will accept the drop.
      onWillAcceptWithDetails: (details) {
        // details.data is the JSON string sent by the draggable:
        // {"src_id": ..., "group": ..., "data": ...}.
        final String payload = details.data;

        // Notify Python side (Flet) about the will_accept event.
        backend.triggerControlEvent(control.id, "will_accept", payload);

        // Optionally enforce group matching on the Flutter side so that
        // only matching groups are accepted.
        try {
          final decoded = jsonDecode(payload);
          final dragGroup = decoded["group"];
          if (dragGroup is String && dragGroup.isNotEmpty) {
            return dragGroup == group;
          }
        } catch (_) {
          // If decoding fails, fall back to allowing the drop.
        }

        return true;
      },

      // Called continuously while a draggable is being moved over this target.
      onMove: (details) {
        final movePayload = jsonEncode({
          "data": details.data,
          "offsetX": details.offset.dx,
          "offsetY": details.offset.dy,
        });

        backend.triggerControlEvent(control.id, "move", movePayload);
      },

      // Called when a draggable is dropped and accepted by this target.
      onAcceptWithDetails: (details) {
        final String payload = details.data;

        // Optionally include drop offset information for the Python side.
        final acceptPayload = jsonEncode({
          "data": payload,
          "offsetX": details.offset.dx,
          "offsetY": details.offset.dy,
        });

        backend.triggerControlEvent(control.id, "accept", acceptPayload);
      },

      // Called when a draggable that was hovering leaves this target.
      onLeave: (payload) {
        backend.triggerControlEvent(control.id, "leave", payload ?? "");
      },

      builder: (
        BuildContext context,
        List<String?> candidateData,
        List<dynamic> rejectedData,
      ) {
        // This is effectively the `content` of the drag target.
        return child;
      },
    );

    return constrainedControl(context, myControl, parent, control);
  }
}
