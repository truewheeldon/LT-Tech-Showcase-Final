import click
import requests
import json


@click.group()
def main():
    pass


@main.command()
@click.option("--albumid", prompt="Album (1-50)", help="Choose a photo album from 1-50.")
def albumid(albumid):

    # check = type(albumid)   # user input valid?
    # if not check.isdigit():  # is not currently functioning, would be nice to have
    #     print("Please run this program again and enter a number from 1-50.")
    #     exit()

    url_format = "https://jsonplaceholder.typicode.com/photos"

    if albumid:     # put only the right chunk of JSON in album object
        query_params = {"albumId": albumid}
        response = requests.get(url_format, params=query_params)
    else:           # otherwise make entire album object the JSON placeholder
        response = requests.get(url_format)

    album_object = json.loads(response.text)

    for album in album_object:       # print to console
        statement = "id: {} | title: {}".format(album["id"], album["title"])
        click.echo(statement)


if __name__ == "__main__":
    main()
