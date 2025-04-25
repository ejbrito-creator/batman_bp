import reflex as rx

class State(rx.State):
    is_dark: bool = True
    hovered_card: str = ""

    def toggle_mode(self):
        self.is_dark = not self.is_dark

    def set_hovered(self, card_name: str):
        self.hovered_card = card_name

def theme_button():
    return rx.button(
        rx.cond(State.is_dark, "☀️ Light", "🌙 Dark"),
        on_click=State.toggle_mode,
        bg=rx.cond(State.is_dark, "white", "black"),
        color=rx.cond(State.is_dark, "black", "white"),
    )

def navbar():
    return rx.box(
        rx.hstack(
            rx.heading("Universo Batman", size="4"),
            rx.spacer(),
            theme_button(),
        ),
        padding="1em",
        bg=rx.cond(State.is_dark, "black", "white"),
        color=rx.cond(State.is_dark, "white", "black"),
        width="100%",
    )

def character_card(name: str, short_desc: str, long_desc: str, image_url: str):
    return rx.box(
        rx.vstack(
            # Frente de la tarjeta (siempre visible)
            rx.box(
                rx.image(
                    src=image_url,
                    width="100%",
                    height="200px",
                    object_fit="cover",
                    border_radius="8px",
                ),
                rx.heading(name, size="4", margin_top="1em"),
                rx.text(short_desc, margin_bottom="1em"),
            ),
            # Parte trasera (solo visible en hover)
            rx.cond(
                State.hovered_card == name,
                rx.box(
                    rx.text(long_desc, padding="1em"),
                    bg=rx.cond(State.is_dark, "gray.700", "gray.200"),
                    border_radius="8px",
                    width="100%",
                ),
            ),
            spacing="2",
        ),
        padding="1em",
        border_radius="8px",
        bg=rx.cond(State.is_dark, "gray.800", "gray.100"),
        color=rx.cond(State.is_dark, "white", "black"),
        box_shadow="lg",
        _hover={
            "transform": "translateY(-10px)",  # Efecto de levitación
            "transition": "transform 0.3s ease",
        },
        on_mouse_enter=lambda: State.set_hovered(name),
        on_mouse_leave=lambda: State.set_hovered(""),
    )

def index():
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.heading("Personajes Principales", size="6"),
            rx.grid(
                character_card(
                    "Batman",
                    "El Caballero Oscuro",
                    "Bruce Wayne lucha contra el crimen en Gotham tras el asesinato de sus padres. Dominio en artes marciales y tecnología.",
                    "https://static.wikia.nocookie.net/batman/images/8/87/Batman_DC_Comics.png",
                ),
                character_card(
                    "Joker",
                    "El Príncipe Payaso del Crimen",
                    "Criminal psicópata con una mente retorcida y sin moral. Archienemigo de Batman.",
                    "https://static.wikia.nocookie.net/batman/images/6/6b/Joker_%28The_Killing_Joke%29.png",
                ),
                character_card(
                    "Catwoman",
                    "Ladrona y antiheroína",
                    "Selina Kyle, una ladrona habilidosa con una relación compleja con Batman.",
                    "https://static.wikia.nocookie.net/batman/images/b/b9/Catwoman_%28Batman_The_Long_Halloween%29.png",
                ),
                columns="3",
                spacing="4",
            ),
            padding="2em",
        ),
        bg=rx.cond(State.is_dark, "gray.900", "gray.50"),
        color=rx.cond(State.is_dark, "white", "black"),
        min_height="100vh",
    )

app = rx.App()
app.add_page(index)