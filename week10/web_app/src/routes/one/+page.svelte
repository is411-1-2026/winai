<script>
    import YourComponent from "#lib/YourComponent.svelte"

    const qa = {
        question: 'พี่เต คือ ใคร?',
        answer: 'ดาวติ๊กต๊อก'
    }
</script>

<h1>Props Example</h1>

<YourComponent question="1+1" answer="2" />
<YourComponent question="อะไรคือ native"  />
<YourComponent question="เนเน่นายแน่มากใครร้อง" answer="หนุ่มบาวสาวปาน" />
<YourComponent {...qa} />