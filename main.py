from class_file.Task_class import Task

import flet as ft

class TodoApp(ft.UserControl):
    def build(self):
            
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True, bgcolor=ft.colors.WHITE, 
                                     border_color=ft.colors.BLUE_900, border_width=1.5, focused_border_color=ft.colors.RED_400, max_length=34)
        self.tasks = ft.Column()

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )
        
        


    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()
    
    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()


def main(page: ft.Page):
    page.title = "ToDo App"
    page.bgcolor = ft.colors.CYAN_100
    page.scroll = ft.ScrollMode.ALWAYS
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    todo = TodoApp()

    # add application's root control to the page
    page.add(todo)

ft.app(target=main)