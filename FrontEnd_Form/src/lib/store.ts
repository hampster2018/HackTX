import { writable } from "svelte/store";

    const id = writable("");
    const questions = writable(["Loading"]);
    const answers = writable("");

export { id, questions, answers };