import type { SvelteComponent } from 'svelte';
import type { Clue } from '..';

declare module 'svelte-crossword' {
    export default class Crossword extends SvelteComponent<{
        data: Clue[];
        storageKey: string;
    }> {}
}