<script>
    import '../styles/main.css';
</script>

<div class="header">
    <a href="/">
        <img class="logo" src="/logo.svg" alt="Miscellany News Logo" />
    </a>
    <a href="/">
        <h1 class="title">Games</h1>
    </a>
</div>

<slot></slot>

<style>
    .header {
        background: var(--color-primary);
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 1rem;
        color: white;
    }

    .logo {
        max-width: 100%;
    }
</style>
