<script lang="ts">
    import { onMount } from 'svelte'
    import App from '../App.svelte'
    import { fade } from 'svelte/transition'
    import { questions, answers } from './store';

    console.log($answers)

    // let contractor = "John"
</script>

<main class="ci-quick">

    <div class="ci-container">
        <p>{$questions[0]}</p>
    </div>
    <div class="ci-ans-container">
        <textarea 
            class="ans-input" 
            placeholder="Aim to write at least two sentences." 
            bind:value={$answers}
        />
    </div>
</main>

<style>

    .ci-quick {
        /* border-style: solid; */
    }

    .ans-input{
        background-color: white;
        border: none;
        box-shadow:4px 4px 4px 2px rgba(5, 5, 82, 0.1);
        border-radius: 4px;
        width: 100%;
        min-height: 100px;
        color: black;
        min-width: 300px;
        max-width: 350px;
        min-height: 50px;
    }

    .ci-ans-container{
        display: flex;
    }

    .ans{
        width: 30%;
        margin: 2%;
        border: solid #81BE1C;
    }

    .ci-container{
        border-radius: 7px;
        margin-bottom: 20px;
        color: black;
        /* background-color: rgb(250, 250, 250); */
        border: solid 1px white;
        box-shadow:4px 4px 4px 5px rgba(5, 5, 82, 0.05);
        border-radius: 4px;
        width: 100%;
        min-height: 75px;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 150%;
    }

    .submit {
        margin: 2%;
        width: 75%;
        background-color: #846954;
        border: none;
        height: 45px;
        border-radius: 8px;
    }

    .submit:focus{
        background-color: #4f3e31;
    }

    #ans-pos{
        background-color: #81BE1C;
    }

    #ans-pos:focus{
        background-color: #5b8615;
    }

    #ans-neu{
        background-color: #81BE1C;
    }

    #ans-neu:focus{
        background-color: #5b8615;
    }

    #ans-neg{
        background-color: #81BE1C;
    }

    #ans-neg:focus{
        background-color: #5b8615;
    }
</style>