import argparse


def main():
    parser = argparse.ArgumentParser(description="Konwerter JSON / YAML / XML")

    parser.add_argument("input_file", help="Plik wejściowy")
    parser.add_argument("output_file", help="Plik wyjściowy")

    args = parser.parse_args()

    print("INPUT:", args.input_file)
    print("OUTPUT:", args.output_file)


if __name__ == "__main__":
    main()