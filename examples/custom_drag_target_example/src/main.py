import os
import sys
import flet as ft

# Ensure we use the local custom_drag_target source from this repo
src_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "src")
)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from custom_drag_target import CustomDragTarget
from custom_draggable import CustomDraggable


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_drag_start(e):
        print(f"Drag started! for {e.control.data} \n")

    def on_drag_cancel(e):
        print("Drag cancelled event received! \n")

    def on_drag_complete(e):
        print("Drag ended event received!\n")

    def on_drag_end(e):
        print("Drag end event received!\n")

    page.add( 
        ft.Container(
            expand=1, alignment = ft.alignment.center, bgcolor=ft.Colors.with_opacity(.1, ft.Colors.PURPLE_200),
            content=CustomDraggable(
                content=ft.Container(content=ft.Row([ft.Icon(ft.Icons.DRAG_HANDLE), ft.Text("Drag me plez")])),
                group="Group 1",    
                data="Data 1", 
                title="Title 1", 
                content_feedback=ft.Text("I'm being dragged!"),
                on_drag_start=on_drag_start,
                on_drag_cancel=lambda e: print("Drag 1 cancelled!"),
                on_drag_complete=lambda e: print("Drag 1 completed!"),
                on_drag_end=lambda e: print("Drag 1 ended!")
            ),
        ),

        ft.Container(
            expand=1, alignment = ft.alignment.center, bgcolor=ft.Colors.with_opacity(.1, ft.Colors.RED_200), 
            content=CustomDraggable(
                content=ft.Text("Draggable 2"),
                group="Group 2",    
                data={'title': 'Title 2'},  
                title="Title 2",
                content_feedback=ft.TextButton("I'm dragging too!"),
                on_drag_start=on_drag_start,
                on_drag_cancel=on_drag_cancel,
                on_drag_complete=on_drag_complete,
                on_drag_end=on_drag_end
            ),
        ),

        ft.Row(
            height=200, expand=True,
            controls=[
                CustomDragTarget(
                    group="Group 1",
                    #title="Drop Target 1",
                    content=ft.TextButton("Drop here (Group 1)"),
                    
                    on_will_accept=lambda e: print(f"Will accept drag for Group 1 e: {e} \n e.data: {e.data}"),
                    on_accept=lambda e: print(f"Accepted drag with data: {e.data}"),
                ),
                CustomDragTarget(
                    group="Group 2",
                    #title="Drop Target 2",
                    content=ft.TextButton("Drop here (Group 2)"),
                    #on_move=lambda e: print(f"Drag moved over target for Group 2 e: {e} \n e.data: {e.data}"),
                    on_will_accept=lambda e: print(f"Will accept drag for Group 2 e: {e} \n e.data: {e.data}"),
                    on_accept=lambda e: print(f"Accepted drag with data: {e.data}"),
                    on_leave=lambda e: print("Drag left the target area."),
                ),
        ])

    ) 


ft.app(main)
