<script lang="ts">
    const PUZZLES: {
        [key: string]: {
            slug: string,
            title: string,
            author: string
            date: string
            progress: number
            size: [number, number]
        }[]
    } = {
        "Fall 2024": [
            {
                "slug": "seasons-greetings",
                "title": "Season's Greetings",
                "author": "Mia Ryan",
                "date": "10/02/24",
                "progress": 0,
                "size": [5, 5],
            },
            {
                "slug": "weekday-1",
                "title": "Weekday #1",
                "author": "Olivia Blank",
                "date": "10/02/24",
                "progress": 0,
                "size": [15, 15],
            },
            {
                "slug": "vassar-bee",
                "title": "Vassar “Bee”",
                "author": "Felix Mundy-Mancino",
                "date": "08/28/24",
                "progress": 0,
                "size": [15, 13],
            }
        ],
        "Spring 2024": []
    }
</script>

<div class="container">
    {#each Object.keys(PUZZLES) as semester}
        <h2 class="semester">{semester}</h2>
        <div class="puzzle-container">
            {#if PUZZLES[semester].length === 0}
                <p><i>Coming soon...</i></p>
            {/if}
            {#each PUZZLES[semester] as { slug, title, author, date, progress, size }}
                <a href="/puzzle/{slug}">
                    <div class="puzzle">
                        <img src="/puzzle-progress-{progress}.svg" alt="Puzzle Icon" />
                        <h3>{title} ({size[0]}x{size[1]})</h3>
                        <p>By <b>{author}</b></p>
                        <p >&middot; <b class="date">{date}</b> &middot;</p>
                    </div>
                </a>
            {/each}
        </div>
    {/each}
</div>

<style>
    .container {
        margin: 1rem;
    }

    .semester {
        margin: 1rem 0;
    }

    .puzzle-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1rem;
    }

    .puzzle {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 1rem;
        border: 1px solid var(--color-primary);
        border-radius: 0.5rem;
        text-align: center;
        transition: background 0.2s ease-out, color 0.2s ease-out;
    }

    .puzzle:hover {
        background: var(--color-primary);
        color: white;
    }
</style>
