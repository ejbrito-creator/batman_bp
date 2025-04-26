import reflex as rx

class State(rx.State):
    hovered_card: str = ""

    def set_hovered(self, card_name: str):
        self.hovered_card = card_name

def navbar():
    return rx.box(
        rx.hstack(
            rx.heading("Universo Batman", size="4", color="black"),
            rx.spacer(),
        ),
        padding="1em",
        bg="white",
        width="100%",
        border_bottom="1px solid #eee",
    )

def character_card(name: str, short_desc: str, long_desc: str, image_url: str):
    return rx.box(
        rx.vstack(
            rx.image(
                src=image_url,
                width="100%",
                height="200px",
                object_fit="cover",
            ),
            rx.heading(name, size="4", margin_top="1em", color="black"),
            rx.text(short_desc, margin_bottom="1em", color="black"),
            rx.cond(
                State.hovered_card == name,
                rx.text(long_desc, padding="1em", color="black"),
            ),
            spacing="2",
            align_items="center",
        ),
        padding="1em",
        border="1px solid #ddd",
        bg="white",
        _hover={
            "box_shadow": "0 4px 8px rgba(0,0,0,0.1)",
        },
        on_mouse_enter=lambda: State.set_hovered(name),
        on_mouse_leave=lambda: State.set_hovered(""),
    )

def index():
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.heading("Personajes Principales", size="6", color="black"),
            rx.grid(
                character_card(
                    "Batman",
                    "El Caballero Oscuro",
                    "Bruce Wayne lucha contra el crimen en Gotham tras el asesinato de sus padres.",
                    "https://cdn.pixabay.com/photo/2024/01/15/11/36/batman-8510022_1280.png",
                ),
                character_card(
                    "Joker",
                    "El Príncipe Payaso del Crimen",
                    "Criminal psicópata con una mente retorcida y sin moral.",
                    "https://cdn.pixabay.com/photo/2024/05/14/09/26/ai-generated-8760744_1280.png",
                ),
                character_card(
                    "Catwoman",
                    "Ladrona y antiheroína",
                    "Selina Kyle, una ladrona habilidosa con una relación compleja con Batman.",
                    "https://w7.pngwing.com/pngs/810/961/png-transparent-catwoman-batman-supervillain-dc-comics-catwoman-catwoman-batman-supervillain.png",
                ),
                columns="3",
                spacing="4",
                width="100%",
                max_width="1200px",
            ),
            padding="2em",
            width="100%",
            align_items="center",
            bg="#f5f5f5",
        ),
        min_height="100vh",
    )

app = rx.App()
app.add_page(index)