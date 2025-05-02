import type { PageServerLoad, Actions } from "./$types";
import { v4 as uuidv4 } from "uuid";
import bcrypt from "bcrypt";

const SALT_ROUNDS = 10;

/**
 * TODO: 
 * check for sessionId. If it exists in the db, redirect eventually.
 * For now do something to indicate this
 */
export const load = (async () => {
  return {};
}) satisfies PageServerLoad;

export const actions = {
  login: async ({ cookies, request }) => {
    const data = await request.formData();
    const phonePlaintext = data.get("phone");
    if (!phonePlaintext) {
      console.log("You have to enter something you fucking idiot");
      return;
    }
    const phoneHash = await bcrypt.hash(phonePlaintext.toString(), SALT_ROUNDS);
    
    const sessionId = uuidv4();
    cookies.set("sessionId", sessionId, { path: "/" });

    console.log(phoneHash);

    // Steps:
    // 1. Retrieve phone number
    //    a. If they didn't enter anything (empty string or null), update form with error message
    // 2. Hash it
    //    a. Check the database for a match. If match, make note of the user_id
    //       Else, update form with error message
    // 3. Generate session id
    // 4. Set the session id cookie, then send the session id to the db
  },
  register: async ({ cookies, request }) => {
    // TODO: perform register
    console.log("Attempt register");

    // Redirect to a registration page. Steps will be similar to login.
  }
} satisfies Actions;
