<script>
    import Thing from "#lib/Thing.svelte"

    let things = $state([
        { id: 1, name: 'egg' },
        { id: 2, name: 'doughnut' },
        { id: 3, name: 'carrot' },
        { id: 4, name: 'banana' },
        { id: 5, name: 'apple' },
        { id: 6, name: 'apple' },
        { id: 7, name: 'apple' },
        { id: 8, name: 'apple' },
    ])
</script>

<button onclick={() => things.pop()}>
    Remove first thing
</button>

{#each things as thing (thing.id)}
    <Thing name={thing.name} />
{/each}