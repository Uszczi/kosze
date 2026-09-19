def main():
    import streamlit as st
    from datetime import date

    from streamlit_calendar import calendar

    st.set_page_config(page_title="Kosze", page_icon="🧺", layout="wide")

    rok = 2026

    frakcje = {
        "Metale i tworzywa": "#f4c430",
        "Papier": "#2d6cdf",
        "Szkło": "#2e9e4f",
        "Bio": "#8b5a2b",
        "Zmieszane": "#555555",
    }

    harmonogram = {
        1: {"Metale i tworzywa": [12], "Papier": [], "Szkło": [13], "Bio": [8], "Zmieszane": [2, 16, 30]},
        2: {"Metale i tworzywa": [9], "Papier": [27], "Szkło": [], "Bio": [5], "Zmieszane": [13, 27]},
        3: {"Metale i tworzywa": [9], "Papier": [], "Szkło": [], "Bio": [5], "Zmieszane": [13, 27]},
        4: {"Metale i tworzywa": [13], "Papier": [], "Szkło": [14], "Bio": [2, 16, 30], "Zmieszane": [10, 24]},
        5: {"Metale i tworzywa": [11], "Papier": [29], "Szkło": [], "Bio": [14, 28], "Zmieszane": [8, 22]},
        6: {"Metale i tworzywa": [8], "Papier": [], "Szkło": [], "Bio": [11, 25], "Zmieszane": [5, 19]},
        7: {"Metale i tworzywa": [13], "Papier": [], "Szkło": [14], "Bio": [9, 23], "Zmieszane": [3, 17, 31]},
        8: {"Metale i tworzywa": [10], "Papier": [28], "Szkło": [], "Bio": [6, 20], "Zmieszane": [14, 28]},
        9: {"Metale i tworzywa": [14], "Papier": [], "Szkło": [], "Bio": [3, 17], "Zmieszane": [11, 25]},
        10: {"Metale i tworzywa": [12], "Papier": [], "Szkło": [13], "Bio": [1, 15, 29], "Zmieszane": [9, 23]},
        11: {"Metale i tworzywa": [9], "Papier": [27], "Szkło": [], "Bio": [12], "Zmieszane": [6, 20]},
        12: {"Metale i tworzywa": [14], "Papier": [], "Szkło": [], "Bio": [3], "Zmieszane": [4, 18]},
    }

    calendar_events = []
    for miesiac, dni_frakcji in harmonogram.items():
        for frakcja, dni in dni_frakcji.items():
            for dzien in dni:
                calendar_events.append(
                    {
                        "title": frakcja,
                        "start": date(rok, miesiac, dzien).isoformat(),
                        "allDay": True,
                        "color": frakcje[frakcja],
                    }
                )

    calendar_options = {
        "editable": False,
        "selectable": True,
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "dayGridDay,dayGridWeek,dayGridMonth",
        },
        "initialView": "dayGridMonth",
        "initialDate": date.today().isoformat(),
        "locale": "pl",
        "locales": [
            {
                "code": "pl",
                "week": {"dow": 1, "doy": 4},
                "buttonText": {
                    "prev": "Poprzedni",
                    "next": "Następny",
                    "today": "Dzisiaj",
                    "year": "Rok",
                    "month": "Miesiąc",
                    "week": "Tydzień",
                    "day": "Dzień",
                    "list": "Plan dnia",
                },
                "weekText": "Tydz",
                "allDayText": "Cały dzień",
                "moreLinkText": "więcej",
                "noEventsText": "Brak wydarzeń",
            },
        ],
    }

    custom_css = """
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
    """

    st.title("Rozpiska koszy")
    st.markdown(
        "<style>.stApp h1 { text-align: center; }</style>",
        unsafe_allow_html=True,
    )

    calendar(
        events=calendar_events,
        options=calendar_options,
        custom_css=custom_css,
        key="calendar",
    )


if __name__ == "__main__":
    main()
