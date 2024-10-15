export type Author = {
    slug: string;
    name: string;
}

export type Clue = {
    clue: string;
    answer: string;
    y: number;
    x: number;
    direction: 'across' | 'down';
}

export type Crossword = {
    slug: string;
    title: string;
    author: Author;
    width: number;
    height: number;
    date: string;
    semester: string;
    data: Clue[];
}
