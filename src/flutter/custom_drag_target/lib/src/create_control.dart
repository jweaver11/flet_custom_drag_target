import 'package:flet/flet.dart';

import 'custom_drag_target.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "custom_drag_target":
      return CustomDragTargetControl(
        parent: args.parent,
        control: args.control,
        children: args.children,
        backend: args.backend,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
