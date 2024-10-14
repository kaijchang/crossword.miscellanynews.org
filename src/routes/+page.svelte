<script>
    const PUZZLES = [
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
    ]
</script>

<div class="container">
    <h2 class="semester">Fall 2024</h2>
    <div class="puzzle-container">
        {#each PUZZLES as { slug, title, author, date, progress, size }}
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
</div>

<style>
    .container {
        margin: 1rem;
    }

    .semester {
        margin-bottom: 1rem;
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
