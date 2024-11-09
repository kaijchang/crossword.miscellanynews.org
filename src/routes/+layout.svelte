<script>
    import { dev } from '$app/environment';
    import { inject } from '@vercel/analytics';

    import '../styles/main.css';

    inject({ mode: dev ? 'development' : 'production' });
</script>

<slot></slot>
