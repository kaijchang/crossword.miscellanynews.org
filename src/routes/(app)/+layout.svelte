<div class="container">
    <div class="header">
        <a href="/">
            <img class="logo" src="/logo.svg" alt="Miscellany News Logo" />
        </a>
        <a href="/">
            <h1 class="title">Crossword</h1>
        </a>
        <!-- <div class="nav-links">
            <h4>
                &middot;
            </h4>
            <h4>
                <a href="/leaderboard">
                    Leaderboard
                </a>
            </h4>
            <h4>
                &middot;
            </h4>
            <h4>
                <a href="/sign-in">
                    Sign In
                </a>
            </h4>
            <h4>
                &middot;
            </h4>
        </div> -->
    </div>
    
    <slot></slot>
    
    <div class="footer">
        <p>
            Questions? Issues? Email <b><a href="mailto:kchang@vassar.edu">kchang@vassar.edu</a></b>
        </p>
    </div>
</div>

<style>
    .container {
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .header, .footer {
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

    .footer {
        margin-top: auto;
    }

    /* .nav-links {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        margin-top: 1em;
        width: 250px;
    } */
</style>
