<script lang="ts">
    import type { PageData } from './$types';

    import Crossword from 'svelte-crossword';

    export let data: PageData;
</script>

<div class="container">
    {#if data.crossword.data !== null}
        <Crossword data={data.crossword.data} />
    {/if}
</div>

<style>
    .container {
        margin: 1rem auto;
        max-width: 800px;
        --xd-primary-highlight-color: #A44E52;
        --xd-secondary-highlight-color: #BE8183;
        --xd-main-color: #030303;
        --xd-bg-color: #ECECEC;
        --xd-accent-color: #D8B3B4;
        --xd-font: 'Open Sans', sans-serif;
    }

    @media(max-width: 720px) {
        .container {
            max-width: 560px
        }
    }
</style>
