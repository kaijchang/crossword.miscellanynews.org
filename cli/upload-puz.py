import os
import puz
import sys
import json
import dotenv
import slugify
import datetime
import requests

dotenv.load_dotenv()

def main():
    """
    property 	type 	description
    clue 	String 	Clue text
    answer 	String 	Answer text (auto-capitalizes)
    direction 	String 	"across" or "down"
    x 	Number 	starting x position (column) of clue
    y 	Number 	starting y position (row) of clue
    custom 	String 	optional custom class name to apply
    """
    p = puz.read(sys.argv[1])

    numbering = p.clue_numbering()
    width = p.width

    data = []

    for clue in numbering.across:
        clue_ = clue['clue']
        answer = ''.join(p.solution[clue['cell'] + i] for i in range(clue['len']))
        direction = 'across'
        x, y = clue['cell'] % width, clue['cell'] // width
        data.append({'clue': clue_, 'answer': answer, 'direction': direction, 'x': x, 'y': y})

    for clue in numbering.down:
        clue_ = clue['clue']
        answer = ''.join(p.solution[clue['cell'] + i * width] for i in range(clue['len']))
        direction = 'down'
        x, y = clue['cell'] % width, clue['cell'] // width
        data.append({'clue': clue_, 'answer': answer, 'direction': direction, 'x': x, 'y': y})

    date = datetime.datetime.strptime(input('Date (YYYY-MM-DD): '), '%Y-%m-%d')
    semester = input('Semester (e.g. fall2024): ')

    authors_data = requests.post(
        os.environ['HYGRAPH_API_URL'],
        json.dumps({
            'query': """query {
                authors {
                    slug
                    name
                }
            }""",
        }),
        headers={
            'Authorization': f'Bearer {os.environ["HYGRAPH_API_TOKEN"]}',
            'Content-Type': 'application/json',
        }
    ).json()

    author_slug = None
    if not p.author:
        p.author = input('Author: ')
    for author in authors_data['data']['authors']:
        if author['name'] == p.author:
            author_slug = author['slug']
            break
    if author_slug is None:
        author_slug = slugify.slugify(p.author)

        create_author_data = requests.post(
            os.environ['HYGRAPH_API_URL'],
            json.dumps({
                'query': """mutation($slug: String!, $name: String!) {
                    createAuthor(data: {
                        slug: $slug,
                        name: $name
                    }) {
                        slug
                        name
                    }
                }""",
                'variables': {
                    'slug': author_slug,
                    'name': p.author,
                }
            }),
            headers={
                'Authorization': f'Bearer {os.environ["HYGRAPH_API_TOKEN"]}',
                'Content-Type': 'application/json',
            }
        ).json()
        print('create author', create_author_data)

        publish_author_data = requests.post(
            os.environ['HYGRAPH_API_URL'],
            json.dumps({
                'query': """mutation($slug: String!) {
                    publishAuthor(where: {
                        slug: $slug
                    }) {
                        slug
                    }
                }""",
                'variables': {
                    'slug': author_slug,
                }
            }),
            headers={
                'Authorization': f'Bearer {os.environ["HYGRAPH_API_TOKEN"]}',
                'Content-Type': 'application/json',
            }
        ).json()
        print('publish author', publish_author_data)
    
    title_slug = slugify.slugify(p.title)

    create_crossword_data = requests.post(
        os.environ['HYGRAPH_API_URL'],
        json.dumps({
            'query': """mutation($slug: String!, $title: String!, $date: DateTime!, $width: Int!, $height: Int!, $data: Json!, $author: AuthorCreateOneInlineInput!, $semester: Semester!) {
                createCrossword(data: {
                    slug: $slug,
                    title: $title,
                    date: $date,
                    width: $width,
                    height: $height,
                    data: $data,
                    author: $author,
                    semester: $semester
                }) {
                    id
                }
            }""",
            'variables': {
                'slug': title_slug,
                'title': p.title,
                'date': date.isoformat() + '-04:00',
                'width': p.width,
                'height': p.height,
                'data': data,
                'author': {
                    'connect': {
                        'slug': author_slug,
                    }
                },
                'semester': semester
            }
        }),
        headers={
            'Authorization': f'Bearer {os.environ["HYGRAPH_API_TOKEN"]}',
            'Content-Type': 'application/json',
        }
    ).json()
    print('create crossword', create_crossword_data)
    
    publish_crossword_data = requests.post(
        os.environ['HYGRAPH_API_URL'],
        json.dumps({
            'query': """mutation($slug: String!) {
                publishCrossword(where: {
                    slug: $slug
                }) {
                    slug
                }
            }""",
            'variables': {
                'slug': title_slug,
            }
        }),
        headers={
            'Authorization': f'Bearer {os.environ["HYGRAPH_API_TOKEN"]}',
            'Content-Type': 'application/json',
        }
    ).json()
    print('publish crossword', publish_crossword_data)

if __name__ == '__main__':
    main()
