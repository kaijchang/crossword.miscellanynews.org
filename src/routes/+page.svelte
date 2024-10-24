<script lang="ts">
    import type { PageData } from './$types';

    import dayjs from 'dayjs';
    import localizedFormat from 'dayjs/plugin/localizedFormat';
    import timezone from 'dayjs/plugin/timezone';

    dayjs.extend(localizedFormat);
    dayjs.extend(timezone);
    dayjs.tz.setDefault('America/New_York');

    export let data: PageData;

    const puzzles: {
        [key: string]: (PageData['crosswords'][number] & { completion?: number, isComplete?: boolean })[]
    } = {}

    $: data.crosswords.forEach(puzzle => {
        let semester = puzzle.semester.slice(0, 4).concat(' ').concat(puzzle.semester.slice(4));
        semester = semester.charAt(0).toUpperCase().concat(semester.slice(1));
        if (!puzzles[semester]) {
            puzzles[semester] = [];
        }

        let completion = 0;
        let isComplete = false;

        if (typeof localStorage !== 'undefined') {
            const storedStateString = localStorage.getItem(`svelte-crossword.${puzzle.slug}`);
            if (storedStateString !== null) {
                const storedState = JSON.parse(storedStateString);
                const percentComplete = storedState.cells.filter((cell: { value: string }) => !!cell.value).length / storedState.cells.length;
                completion = Math.floor(percentComplete * 16);
                isComplete = storedState.cells.every((cell: { value: string, answer: string }) => cell.value === cell.answer);
            }
        }

        puzzles[semester].push({
            ...puzzle,
            completion,
            isComplete
        });
    });
</script>

<svelte:head>
    <title>Crossword - The Miscellany News</title> 
</svelte:head>

<div class="container">
    {#each Object.keys(puzzles) as semester}
        <h2 class="semester">{semester}</h2>
        <div class="puzzle-container">
            {#if puzzles[semester].length === 0}
                <p><i>Coming soon...</i></p>
            {/if}
            {#each puzzles[semester] as { slug, title, author, date, width, height, data, completion, isComplete }}
                <a href={data && `/puzzle/${slug}`}>
                    <div class="puzzle" class:disabled={data === null}>
                        <img
                            class="puzzle-icon"
                            src="/puzzle-progress-{isComplete ? 'complete' : completion}.svg"
                            alt="Puzzle Icon"
                            height="97"
                        />
                        <h3>{title} ({width}x{height})</h3>
                        <p>By <b>{author.name}</b></p>
                        <p >&middot; <b class="date">{dayjs(date).format('L')}</b> &middot;</p>
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

    .puzzle:not(.disabled):hover {
        background: var(--color-primary);
        color: white;
    }

    .disabled {
        cursor: not-allowed;
        opacity: 0.4;
    }

    .puzzle-icon {
        border-radius: 0.25em;
    }
</style>
