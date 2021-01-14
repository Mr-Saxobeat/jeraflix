<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
    <a class="navbar-brand" href="/">Jeraflix</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">

            <li class="nav-item">
                <a class="nav-link" href="/">Populares <span class="sr-only">(current)</span></a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/watchlist/">Minha Lista</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/watched/">Assistidos</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/search/">Buscar</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/accounts/logout/">Sair</a>
            </li>
            
        </ul>
    </div>
    </div>  
</nav>
</template>

<script>
export default {
    name: "NavbarComponent"
}
</script>

<style >

</style>