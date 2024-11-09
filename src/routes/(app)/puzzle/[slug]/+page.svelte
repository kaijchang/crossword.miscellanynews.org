<script lang="ts">
    import type { PageData } from './$types';
    import { page } from '$app/stores';

    import Crossword from 'svelte-crossword';

    export let data: PageData;
</script>

<svelte:head>
    <title>{data.crossword.title} - Crossword - The Miscellany News</title> 
</svelte:head>

<div class="container">
    {#if data.crossword.data !== null}
        <Crossword data={data.crossword.data} storageKey={$page.params.slug} />
    {/if}
</div>

<style>
    .container {
        margin: 1rem auto;
        max-width: 800px;
    }

    @media(max-width: 720px) {
        .container {
            max-width: 560px
        }
    }

    @media(max-width: 560px) {
        .container {
            max-width: calc(100% - 1em);
        }
    }
</style>
