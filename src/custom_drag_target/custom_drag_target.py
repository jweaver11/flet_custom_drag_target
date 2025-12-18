from enum import Enum
from typing import Any, Optional
from flet.core.control import Control

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber

class CustomDragTarget(ConstrainedControl):
    """
    CustomDragTarget Control description.
    """

    def __init__(
        self,
        #
        # All flet controls 
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # Flet Constrained controls Specific (ConstrainedControl)
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        #
        # Anything custom we want to pass in (Custom Drag Target specific)
        #
        group: str = "",
        title: str = "Drag Me",     
        on_will_accept = None,    
        on_move = None,  
        on_accept = None,
        on_leave = None,
        content: Control | None = None,     
    ):
        ConstrainedControl.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        # Title and group used to identify drag target
        self.title = title
        self.group = group

        # Event handlers
        self.on_will_accept = on_will_accept
        self.on_move = on_move
        self.on_accept = on_accept
        self.on_leave = on_leave

        # Content for inside the drag target
        self.content = content

    def _get_control_name(self):
        return "custom_drag_target"

    ''' Group property for the draggable '''
    @property
    def group(self) -> str:
        return self._get_attr("group")
    
    @group.setter
    def group(self, value: str):
        self._set_attr("group", value)


    ''' Title property for the draggable '''
    @property
    def title(self) -> str:
        return self._get_attr("title")
    
    @title.setter
    def title(self, value: str):
        self._set_attr("title", value)


    ''' Event handler for the on_will_accept event '''
    @property
    def on_will_accept(self):
        return self._get_event_handler("will_accept")   
    
    @on_will_accept.setter
    def on_will_accept(self, handler):
        self._add_event_handler("will_accept", handler)


    ''' Event handler for the on_enter event '''
    @property
    def on_move(self):
        return self._get_event_handler("move")
    
    @on_move.setter
    def on_move(self, handler):
        self._add_event_handler("move", handler)


    ''' Event handler for the on_accept event '''
    @property
    def on_accept(self):
        return self._get_event_handler("accept")
    
    @on_accept.setter
    def on_accept(self, handler):
        self._add_event_handler("accept", handler)

    ''' Event handler for the on_leave event '''
    @property
    def on_leave(self):
        return self._get_event_handler("leave")
    
    @on_leave.setter
    def on_leave(self, handler):
        self._add_event_handler("leave", handler)

    ''' Content property for the drag target'''
    @property
    def content(self) -> Control:
        # stored locally; returned as a named child via _get_children()
        return self._content

    @content.setter
    def content(self, value: Control):
        self._content = value

    def _get_children(self):
        children = []
        if self._content:
            self._content._set_attr_internal("n", "content")
            children.append(self._content)
        return children