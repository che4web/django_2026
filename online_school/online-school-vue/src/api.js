
import axios from "axios";

export default function toURLParams(filters) {
  let params = new URLSearchParams();
  for (let f in filters) {
    if (Array.isArray(filters[f])) {
      for (let p of filters[f]) {
        if (p) {
          if (p.id) {
            params.append(f, p.id);
          } else {
            params.append(f, p);
          }
        }
      }
    } else if (filters[f] && filters[f].id) {
      params.append(f, filters[f]['id'])

    } else {
      if (filters[f] != undefined) {
        params.append(f, filters[f]);
      }

    }
  }
  return params
}

async function _save(url, obj) {
  let response;
  let id;
  if (obj instanceof FormData) {
    id = obj.get("id");
  } else {
    id = obj.id;
  }

  if (id) {
    response = await axios.patch(url + id + "/", obj);
  } else {
    response = await axios.post(url, obj);
  }
  return response.data;
}
async function _delete(url, obj) {
  let response;
  if (obj.id) {
    response = await axios.delete(url + obj.id + "/", obj);
  }

  return response;
}

async function _getList(url, filter, params = {}) {
  const response = await axios.get(url + "?" + toURLParams(filter), params);
  return response.data;
}

async function _getById(url, id) {
  const response = await axios.get(url + id + "/");
  return response.data;
}


function apiConstructor(apiUrl) {
  return {
    async save(obj) {
      return _save(apiUrl, obj);
    },
    async getById(obj) {
      return _getById(apiUrl, obj);
    },
    async getList(filter, params = {}) {
      return _getList(apiUrl, filter, params);
    },
    async delete(obj) {
      return _delete(apiUrl, obj);
    },
  };
}

export let Lesson = apiConstructor("/api/lesson/")
export let LessonTypes = apiConstructor("/api/lesson/types/")
export let LessonMaterial = apiConstructor("/api/lesson_material/")
