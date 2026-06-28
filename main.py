import argparse
import json


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Błąd: plik nie istnieje")
        return None
    except json.JSONDecodeError:
        print("Błąd: niepoprawny JSON")
        return None


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file")
    parser.add_argument("output_file")

    args = parser.parse_args()

    data = load_json(args.input_file)

    if data is None:
        return

    print("Wczytane dane:")
    print(data)


if __name__ == "__main__":
    main()