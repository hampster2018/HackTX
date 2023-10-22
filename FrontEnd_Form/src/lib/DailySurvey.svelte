<script lang="ts">
    import AdditionalComments from './AdditionalComments.svelte';
    import QuickCi from './QuickCi.svelte'
    import ShortCi from './ShortCi.svelte'
    import SlideCi from './SlideCi.svelte'
    import { fade } from 'svelte/transition'
    import postAnswer from './PostData'
    import { id, questions, answers } from './store'
  
    let user = "John";
    let quick = 0;
    let short = 1;
    let slide = 0;
  
    let animate = false
  
  </script>
  
  <!-- <svelte:head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
  </svelte:head> -->
  
  <main class="master-container">
    <div class="wel-msg">
      <p class="wel-msg-txt1">Hi, {user}!</p>
      <p class="wel-msg-txt2">Let's complete your daily checkin.</p>
    </div>
  
    <div class="ci-question-container">
      <svelte:component this={quick ? QuickCi : null}/>
      <svelte:component this={short ? ShortCi  : null}/>
      <svelte:component this={slide ? SlideCi : null}/>
    </div>
  
    
    <AdditionalComments/>

    <div class="ci-submit-container">
        <input class="submit" type="submit" value="Submit" on:click={(e) => postAnswer($id, $questions[0], $answers)}>
    </div>
    
  </main>
  
  <style>
    .ci-submit-container {
        background-color: green;
        padding-bottom: 20px;
    }

    .add-container{
      /* border: solid 1px; */
    }

    .submit {
        margin-top: 0%;
        width: 100%;
        background-color: #846954;
        border: none;
        height: 45px;
        border-radius: 8px;
    }

    .submit:focus{
        background-color: #4f3e31;
    }
  
    .wel-msg-txt1{
      font-weight: 700;
      font-size: 150%;
      line-height: normal;
      margin-bottom: 2%;
      
      /* border: solid 1px; */
    }
  
    .wel-msg-txt2{
      font-size: 60%;
      /* display: flex; */
      line-height: normal;
      
    }
  
    .add-input{
      margin-bottom: 50px;
      color: black;
    }
  
    .wel-msg{
      /* border: solid 1px; */
      /* display: flex; */
      font-size: 175%;
      font-weight: 600;
      display: inline;
    }
  
    .add-accord{
      /* border: solid 1px; */
      margin-top: 12%;
      height: 40px;
      border-radius: 5px;
      font-weight: 400;
      padding: 8%;
      color: black;
    }
  
    .add-input{
      background-color: white;
      background-color: white;
      border: none;
      box-shadow:4px 4px 4px 2px rgba(5, 5, 82, 0.1);
      border-radius: 4px;
      width: 100%;
      min-height: 100px;
    }
  </style>