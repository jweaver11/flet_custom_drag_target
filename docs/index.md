# Introduction

CustomDragTarget for Flet.

## Examples

```
import flet as ft

from custom_drag_target import CustomDragTarget


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=CustomDragTarget(
                    tooltip="My new CustomDragTarget Control tooltip",
                    value = "My new CustomDragTarget Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[CustomDragTarget](CustomDragTarget.md)


