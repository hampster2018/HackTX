<script lang="ts">
  import DailySurvey from "./lib/DailySurvey.svelte";
  import Survey from "./lib/Survey.svelte";
  import Questions from "./lib/Questions.svelte";
  import {onMount} from 'svelte'
  import { id } from "./lib/store";

  id.set((window.location.href).split('=')[1])
  console.log($id)

  let user = "Joshua";
  let foreman = "Mike";
  let quick = 1;
  let short = 0;
  let slide = 0;
  let dailyFlag = 1;
  let weeklyFlag = 0;

  let animate = false;

</script>

<!-- <svelte:head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
</svelte:head> -->

<main class="master-container">
    <svelte:component this={dailyFlag ? DailySurvey : null}/>
    <svelte:component this={weeklyFlag ? Survey  : null}/>
    
    <Questions/>
</main>

<style>
  .master-container{
        /* border-style: solid; */
        animation: fadeInAnimation ease 3s;
        animation-iteration-count: 1;
        animation-fill-mode: forwards;
    } @keyframes fadeInAnimation { 
        0% { 
            opacity: 0; 
        } 100% { 
            opacity: 1; 
        } 
  }
</style>