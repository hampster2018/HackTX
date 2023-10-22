<script lang="ts">
  import { onMount } from 'svelte'
  import App from '../App.svelte'
  import { fade } from 'svelte/transition'


  let q_txt = "How has your satistifaction been with your daily tasks at work recently?"
  let ans1 = "Good"
  let ans2 = "Okay"
  let ans3 = "Bad"
  let min = 0;
  let max = 10;
  let step = 1;
  let val = 5;
  let q = "On a scale of 1 to 10 how satisfied are you with your vacation and time off?"
  let slide_ex = "(1 = not satisifed at all, 10 = very satisfied)"
  let ready = false;
  onMount(() => ready = true);

  export const user = () => console.log('test');
</script>

<main class="ci-quick">
  <div class="ci-container">
    <p>{q}</p>
    <p class="ci-sub">{slide_ex}</p>
  </div>
    
  <p class="val">{val}</p>
  <input 
    class="slider"
    type="range"
    {min}
    {max}
    {step}
    bind:value={val}
  />
  
  


  
</main>

<style>
  .slider{
    background-color: #81BE1C;
    --track-highlight-bgcolor: #C368FF;
    /* border: solid 5px black; */
  }

  .ci-ans-container{
      /* display: flex; */
  }

  .val{
    font-weight: 600;
    font-size: 25px;
  }

  .ci-sub{
    font-size: 15px;
    font-weight: 500;
    line-height: 1;
  }

  .ans{
      width: 100%;
      margin-top: 6%;
      /* margin: 2%; */
      border: solid #81BE1C;
      color: white;
  }

  .ci-container{
      /* border: solid 1px; */
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
      /* display: inline; */
      /* justify-content: inline; */
      
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