import click
import requests


@click.group()
def cli():
    pass


@cli.command()
def view_feed():
    """Display posts from the feed."""
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    if resp.status_code == 200:
        for post in resp.json():
            click.echo("" * 20)
            click.echo("Title: " + post['title'])
            click.echo("" * 20)
            click.echo("Body: " + post['body'])
            click.echo("" * 20)


@cli.command()
@click.argument("title")
@click.argument("body")
def post(title, body):
    """Submit a new post to the feed."""
    data = {
        "title": title,
        "body": body
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
    click.echo("Response: " + str(response.status_code))
    click.echo(data)


@cli.command()
@click.argument('post_id')
def view_comments(post_id):
    """Display a posts's comments."""
    response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=" + "{}".format(post_id))
    click.echo(response.status_code)
    for comment in response.json():
        click.echo("" * 20)
        click.echo("Email: " + comment["email"])
        click.echo("Body: " + comment["body"])
        click.echo("" * 20)


@cli.command()
@click.argument('post_id')
@click.argument('title')
@click.argument('body')
def comment(post_id, title, body):
    """Add a comment to a post."""
    data = {
        "postId": post_id,
        "title": title,
        "body": body
    }

    response = requests.post("https://jsonplaceholder.typicode.com/comments?postId=" + "{}".format(post_id), data=data)
    click.echo(response.status_code)
    click.echo(data)
