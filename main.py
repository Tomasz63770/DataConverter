import argparse
import json
import os
import yaml
import xmltodict
from dicttoxml import dicttoxml


# ---------------- JSON ----------------
def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        print("JSON error: invalid JSON syntax in file.")
        return None
    except FileNotFoundError:
        print("JSON error: file not found.")
        return None
    except Exception as e:
        print(f"JSON error: {e}")
        return None


def save_json(file_path, data):
    try:
        if data is None:
            print("JSON save error: no data to save.")
            return

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    except TypeError:
        print("JSON save error: data is not serializable.")
    except Exception as e:
        print(f"JSON save error: {e}")


# ---------------- YAML ----------------
def load_yaml(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data

    except yaml.YAMLError:
        print("YAML error: invalid YAML syntax in file.")
        return None
    except FileNotFoundError:
        print("YAML error: file not found.")
        return None
    except Exception as e:
        print(f"YAML error: {e}")
        return None


def save_yaml(file_path, data):
    try:
        if data is None:
            print("YAML save error: no data to save.")
            return

        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)

    except yaml.YAMLError:
        print("YAML save error: invalid YAML format.")
    except Exception as e:
        print(f"YAML save error: {e}")


# ---------------- XML ----------------
def load_xml(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return xmltodict.parse(f.read())
    except Exception as e:
        print(f"XML error: {e}")
        return None


def save_xml(file_path, data):
    try:
        xml_bytes = dicttoxml(data, custom_root="root", attr_type=False)
        with open(file_path, "wb") as f:
            f.write(xml_bytes)
    except Exception as e:
        print(f"XML save error: {e}")


# ---------------- MAIN ----------------
def main():
    parser = argparse.ArgumentParser(description="Data Converter JSON/YAML/XML")

    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' does not exist.")
        return

    input_file = args.input_file.lower()
    output_file = args.output_file.lower()

    # -------- INPUT --------
    if input_file.endswith(".json"):
        data = load_json(args.input_file)

    elif input_file.endswith((".yaml", ".yml")):
        data = load_yaml(args.input_file)

    elif input_file.endswith(".xml"):
        data = load_xml(args.input_file)

    else:
        print("Unsupported input format.")
        return

    if data is None:
        print("Failed to load input data.")
        return

    print("Wczytane dane:", data)

    # -------- OUTPUT --------
    if output_file.endswith(".json"):
        save_json(args.output_file, data)

    elif output_file.endswith((".yaml", ".yml")):
        save_yaml(args.output_file, data)

    elif output_file.endswith(".xml"):
        save_xml(args.output_file, data)

    else:
        print("Unsupported output format.")
        return

    print("Zapisano do:", args.output_file)


if __name__ == "__main__":
    main()