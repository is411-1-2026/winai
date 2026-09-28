<script>
    import Quantifier from '$lib/Quantifier.svelte'

    let name = 'Winai Nadee'
    let imageUrl = 'https://avatars.githubusercontent.com/u/20796183'
    let string = 'this string contains some <strong>HTML!!!</strong>'
</script>

<h1>Welcome to IS411</h1>
<div>
    <p>Name: {name}</p>
    <p>Week 09</p>
    <p>Example 1</p>
    <p>{@html string}</p>
    <img height="200" src={imageUrl} alt={name}>

</div>
<Quantifier />

<style>
    p {
        color: brown;
        font-family: 'Comic Sans MS', cursive;
        font-size: 2em;
    }
    h1 {
        color: crimson;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
</style>
