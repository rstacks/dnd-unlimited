import { BACKEND_URL, API_KEY } from "$env/static/private";
import { error } from "@sveltejs/kit";

export interface ClassData {
  id: number;
  class_name: string;
  class_desc: string;
  hit_dice: string;
  feat_name: string;
  feat_desc: string;
  saves: string[];
  skills: string[];
}

interface ClassesJSON {
  classes: ClassData[];
}

export async function getClasses(): Promise<ClassData[]> {
  const resp = await fetch(BACKEND_URL + "/classes", {
    headers: { "Authorization": "Bearer " + API_KEY }
  });
  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
  const classJson: ClassesJSON = await resp.json()
  const allClasses = classJson.classes;
  return allClasses;
}
