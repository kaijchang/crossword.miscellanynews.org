<script>
    import Crossword from 'svelte-crossword';

    const data = [
        {
            "clue": "Reddit forum featuring a famous person",
            "answer": "AMA",
            "direction": "across",
            "x": 0,
            "y": 0
        },
        {
            "clue": "Greeting in Oaxaca",
            "answer": "HOLA",
            "direction": "across",
            "x": 0,
            "y": 1
        },
        {
            "clue": "British kisses",
            "answer": "SNOGS",
            "direction": "across",
            "x": 0,
            "y": 2
        },
        {
            "clue": "White whale hunter",
            "answer": "AHAB",
            "direction": "across",
            "x": 1,
            "y": 3
        },
        {
            "clue": "Dog noise",
            "answer": "ARF",
            "direction": "across",
            "x": 2,
            "y": 4
        },
        {
            "clue": "Noises of realization",
            "answer": "AHS",
            "direction": "down",
            "x": 0,
            "y": 0
        },
        {
            "clue": "___ Lisa",
            "answer": "MONA",
            "direction": "down",
            "x": 1,
            "y": 0
        },
        {
            "clue": "Honolulu hello",
            "answer": "ALOHA",
            "direction": "down",
            "x": 2,
            "y": 0
        },
        {
            "clue": "Lab jelly",
            "answer": "AGAR",
            "direction": "down",
            "x": 3,
            "y": 1
        },
        {
            "clue": "Infamous crypto bro (abbr.)",
            "answer": "SBF",
            "direction": "down",
            "x": 4,
            "y": 2
        },
    ];
</script>

<div class="container">
    <Crossword data='{data}' />
</div>

<style>
    .container {
        margin: 1rem auto;
        max-width: 800px;
    }
</style>
