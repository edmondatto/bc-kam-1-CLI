import click
import requests

"""
A command line application that parses json from newsapi.org
"""


@click.command()
def cli():
    """
    Stuck? Here's some help! 
    """
    draw_header()
    greeting()

    news_request = requests.get(
        "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=8ddc75bfec6b470a85fb69bccce7afbb")
    main_dict = news_request.json()
    article_list = main_dict['articles']

    for article in article_list:
        click.echo(click.style('TITLE: ' + article['title'], fg='green'))
        click.echo(click.style('BY: ' + article['author'], fg='blue'))
        click.echo('\n')
        click.echo(click.wrap_text(article['description'], 100))
        click.echo('\n')
        click.echo('-' * 100)


def greeting():
    print("Hi there, I'm Vortex, your news buddy! You can count on me to keep you posted.")
    user_name = input('> What\'s your name?: ')
    print('\nIt\'s nice to meet you {}. I\'ll have the latest news stories for you in a jiff: \n'.format(user_name))
    print('-' * 100)


def draw_header():
    click.echo('\n')
    click.echo(click.style('*' * 100, fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 32 + 'WELCOME TO THE VORTEX NEWS PORTAL ' + ' ' * 32 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='green'))
    click.echo(click.style('*' * 100, fg='green'))
    click.echo('\n')
