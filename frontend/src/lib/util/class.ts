import { BACKEND_URL, API_KEY } from "$env/static/private";

interface ClassData {
  id: number;
  class_name: string;
  class_desc: string;
  hit_dice: string;
  feat_name: string;
  feat_desc: string;
  saves: string[];
  skills: string[];
}


