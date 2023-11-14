import flet as ft
from flet_core.ref import T
from class_file.DB_class import DBClass

class Task(ft.UserControl):
    def __init__(self, task_name, task_delete, check_flg, db_id):
        super().__init__()
        self.db_id = db_id
        self.task_name   = task_name
        self.task_delete = task_delete
        if check_flg == 0:
            self.check_flg = False
        else:
            self.check_flg = True
        


    def build(self):
        def checkbox_changed(e):
            DBClass.update_flg(flg=self.display_task.value, id=self.db_id)
            
        self.display_task = ft.Checkbox(label=self.task_name, value=self.check_flg, on_change=checkbox_changed)
        self.edit_name    = ft.TextField(expand=1, bgcolor=ft.colors.WHITE, border_width=1.5, focused_border_color=ft.colors.RED_400, max_length=34)

        self.display_view = ft.Row(
            alignment          = ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            
            controls = [
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])


    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()


    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
        DBClass.update_task(task_value=self.edit_name.value, id=self.db_id)
    
    
    def delete_clicked(self, e):
        self.task_delete(self)
        DBClass.delete(id=self.db_id)