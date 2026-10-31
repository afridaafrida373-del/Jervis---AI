
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from datetime import datetime

Window.clearcolor = (0.015, 0.025, 0.08, 1)

class JarvisApp(App):
    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        self.title = "JARVIS AI"

        title = Label(
            text="[b]J.A.R.V.I.S[/b]",
            markup=True,
            font_size=38,
            color=(0.1, 0.75, 1, 1),
            size_hint_y=0.2
        )
        root.add_widget(title)

        self.status = Label(
            text="SYSTEM ONLINE\nHow can I help you?",
            font_size=20,
            color=(0.3, 0.85, 1, 1)
        )
        root.add_widget(self.status)

        self.output = Label(
            text="Hello! I am your JARVIS assistant.",
            font_size=18
        )
        root.add_widget(self.output)

        self.command = TextInput(
            hint_text="Type your command...",
            multiline=False,
            size_hint_y=0.15
        )
        root.add_widget(self.command)

        btn = Button(
            text="EXECUTE COMMAND",
            size_hint_y=0.15,
            background_color=(0, 0.4, 0.8, 1)
        )
        btn.bind(on_press=self.execute)
        root.add_widget(btn)

        return root

    def execute(self, instance):
        cmd = self.command.text.lower().strip()

        if "time" in cmd or "সময়" in cmd:
            answer = datetime.now().strftime("%I:%M %p")

        elif "date" in cmd or "তারিখ" in cmd:
            answer = datetime.now().strftime("%d-%m-%Y")

        elif "hello" in cmd or "হ্যালো" in cmd:
            answer = "Hello! JARVIS is ready."

        elif "your name" in cmd:
            answer = "I am JARVIS, your AI assistant."

        elif "help" in cmd or "সাহায্য" in cmd:
            answer = "Try: time, date, hello, help."

        else:
            answer = "Offline command not recognized."

        self.output.text = answer
        self.command.text = ""

JarvisApp().run()
