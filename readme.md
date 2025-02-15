# My Markdown File

This is some Markdown text. Below is the HTML code for displaying a logo and title.

<style>
    
    @font-face {
        font-family: 'WatchmenFont';
        src: url('src/watchmen.ttf') format('woff2'),
        url('src/watchmen.ttf') format('woff');
        font-weight: normal;
        font-style: normal;
    }

    body {
        margin: 0;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: transparent;
    }

    .container {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .logo {
        width: 50px;
        height: auto;
    }

    .title {
        font-size: 24px;
        font-family: 'WatchmenFont', Arial, sans-serif;
        color: #ffeb00;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
</style>

<div class="container">
    <img src="src/logo.png" alt="Logo" class="logo">
    <h1 class="title">WebMonitor</h1>
</div>

This is more Markdown text below the HTML.