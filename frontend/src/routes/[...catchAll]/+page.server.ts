import type { PageServerLoad } from "./$types";
import { redirect } from "@sveltejs/kit";

export const load = (() => {
  redirect(303, "/dashboard");
}) satisfies PageServerLoad;