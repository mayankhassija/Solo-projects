from src.services import create_note

def main():
    path = create_note(
        "My First Note",
        "Hello from AI Memory OS!"
    )

    print(f"Saved: {path}")

if __name__ == "__main__":
    main()

    