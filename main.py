import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Program do konwersji plików JSON, YAML i XML"
    )

    parser.add_argument("input_file", help="Plik wejściowy")
    parser.add_argument("output_file", help="Plik wyjściowy")

    args = parser.parse_args()

    print("Plik wejściowy:", args.input_file)
    print("Plik wyjściowy:", args.output_file)


if __name__ == "__main__":
    main()