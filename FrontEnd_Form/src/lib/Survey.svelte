<script lang="ts">
    import { onMount } from 'svelte'
    import App from '../App.svelte'
    import { fade } from 'svelte/transition'
    import QuickCi from './QuickCi.svelte';
    import ShortCi from './ShortCi.svelte';
    import SlideCi from './SlideCi.svelte';
    import AdditionalComments from './AdditionalComments.svelte';
    import postAnswer from './PostData'
    import { id, questions, answers } from './store'
    import QuickCi_2 from './QuickCi_2.svelte';
    import ShortCi_2 from './ShortCi_2.svelte';

    let user = "John";
    let q_types = [""];
    let numQuestions = 4;
    let foreman = "Mike";
    q_types = ["short", "quick", "slide", "quick2", "short2"];

</script>

<main class="survey-container">
    <div class="wel-msg">
        <p class="wel-msg-txt1">Hi, {user}!</p>
        <p class="wel-msg-txt2">Let's complete your weekly check-in.</p>
    </div>

    <div class="ci-question-container">
        {#each q_types as q_type}
            {#if q_type == "quick"}
                <div class="q-container">
                    <QuickCi/>
                </div>
            {:else if q_type == "short"}
                <div class="q-container">
                    <ShortCi/>
                </div>
            {:else if q_type == "slide"}
                <div class="q-container">
                    <SlideCi/>
                </div>
            {:else if q_type == "quick2"}
                <div class="q-container">
                    <QuickCi_2/>
                </div>
            {:else if q_type == "short2"}
                <div class="q-container">
                    <ShortCi_2/>
                </div>
            {:else}
                <p>error</p>
            {/if}
        {/each}
    </div>

    <AdditionalComments/>

    <div class="ci-submit-container">
        <input class="submit" type="submit" value="Submit" on:click={(e) => postAnswer($id, $questions[0], $answers)}>
    </div>

    

</main>

<style>
    .wel-msg-txt1{
      font-weight: 800;
      font-size: 150%;
      line-height: normal;
      margin-bottom: 2%;
      
      /* border: solid 1px; */
    }

    .submit {
        margin-top: 0%;
        width: 100%;
        background-color: #846954;
        border: none;
        height: 45px;
        border-radius: 8px;
        color: white;
        font-size: 20px;
    }

    .submit:focus{
        background-color: #4f3e31;
    }

    .ci-question-container{
        margin-top: 15%;
    }
  
    .wel-msg-txt2{
      font-size: 60%;
      /* display: flex; */
      line-height: normal;
      
    }

    .q-container{
        /* border: solid 1px; */
        margin-top: 20%;
        box-shadow: 4px 4px 4px 4px rgba(5, 5, 82, 0.05);
        padding: 5%;
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