<script>
    const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    let selected = $state(colors[0])
</script>

<h1 style="color: {selected}">Pick a color</h1>

<div>
    {#each colors as color, i}
        <button
            style="background: {color}"
            aria-label={color}
            aria-current={selected === color}
            onclick={() => selected = color}
        >{i + 1}</button>
    {/each}
</div>