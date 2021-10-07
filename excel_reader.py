"""
Usage: script.py [OPTIONS]

  file_name is required to provided from command line. e.g. 'https://github.
  com/amitsinghpgs/freelancer_amit/blob/main/20210929%20-%20Korian%20-%20Inv
  entaire%20ISIM-Wallix.xlsx?raw=true'

Options:
  --file_name TEXT  enter local file name or web link to an excel file
                    [required]

  --help            Show this message and exit.

e.g.
python excel_reader.py --file_name 'https://github.com/amitsinghpgs/freelancer_amit/blob/main/20210929%20-%20Korian%20-%20Inventaire%20ISIM-Wallix.xlsx?raw=true'
python excel_reader.py --file_name '20210929 - Korian - Inventaire ISIM-Wallix.xlsx'
  """
import pandas as pd
import click


@click.command()
@click.option(
    "--file_name",
    help="enter local file name or web link to an excel file",
    required=True,
)
def main(file_name):
    """
    file_name is required to provided from command line. e.g.
    'https://github.com/amitsinghpgs/freelancer_amit/blob/main/20210929%20-%20Korian%20-%20Inventaire%20ISIM-Wallix.xlsx?raw=true'
    """
    df = pd.read_excel(file_name, engine="openpyxl",)

    print(df.to_csv(index=False))


if __name__ == "__main__":
    main()
