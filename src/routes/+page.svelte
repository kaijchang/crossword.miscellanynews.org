<script lang="ts">
    import type { PageData } from './$types';

    import moment from 'moment';

    export let data: PageData;

    const puzzles: {
        [key: string]: PageData['crosswords']
    } = {}

    $: data.crosswords.forEach(puzzle => {
        let semester = puzzle.semester.slice(0, 4).concat(' ').concat(puzzle.semester.slice(4));
        semester = semester.charAt(0).toUpperCase().concat(semester.slice(1));
        if (!puzzles[semester]) {
            puzzles[semester] = [];
        }
        puzzles[semester].push(puzzle);
    });
</script>

<div class="container">
    {#each Object.keys(puzzles) as semester}
        <h2 class="semester">{semester}</h2>
        <div class="puzzle-container">
            {#if puzzles[semester].length === 0}
                <p><i>Coming soon...</i></p>
            {/if}
            {#each puzzles[semester] as { slug, title, author, date, width, height }}
                <a href="/puzzle/{slug}">
                    <div class="puzzle">
                        <img src="/puzzle-progress-0.svg" alt="Puzzle Icon" />
                        <h3>{title} ({width}x{height})</h3>
                        <p>By <b>{author.name}</b></p>
                        <p >&middot; <b class="date">{moment(date).format('L')}</b> &middot;</p>
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
