<template>
  <form @submit.prevent="handleSubmit">
    <label>Email:</label>
    <input type="email" v-model="email" required />
    <label>password:</label>
    <input type="password" v-model="password" required />
    <div v-if="passwordError" class="error">
      {{ passwordError }}
    </div>

    <label>role</label>
    <select v-model="role">
      <option value="backend">Backend Engineer</option>
      <option value="designer">Web Designer</option>
      <option value="developer">Web Deveoper</option>
    </select>

    <label>skills (type your skills seperated by comma)</label>
    <input type="text" v-model="tempSkill" @keyup="addSkill" />
    <div
      v-for="(skill, index) in skills"
      :key="skill"
      class="pill"
      @click="deleteSkill(index)"
    >
      {{ skill.replace(/,/g, "") }}
    </div>

    <div class="terms">
      <input type="checkbox" v-model="terms" required />
      <label>accept terms</label>
    </div>
    <div class="submit">
      <button>Sign Up</button>
    </div>
    <div>
      <input type="checkbox" value="saki" v-model="names" />
      <label>Saki</label>
    </div>
    <div>
      <input type="checkbox" value="ruby" v-model="names" />
      <label>Ruby</label>
    </div>
    <div>
      <input type="checkbox" value="yuki" v-model="names" />
      <label>Yuki</label>
    </div>
  </form>

  <div class="output">
    <p>email {{ email }}</p>
    <p>password {{ password }}</p>
    <p>terms {{ terms }}</p>
    <p>role {{ role }}</p>
    <p>names {{ names }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      role: "backend",
      terms: false,
      names: [],
      tempSkill: "",
      skills: [],
      passwordError: "",
    };
  },
  methods: {
    addSkill(event) {
      if (event.key === "," && this.tempSkill) {
        if (!this.skills.includes(this.tempSkill)) {
          this.skills.push(this.tempSkill);
        }
        this.tempSkill = "";
      }
    },
    deleteSkill(index) {
      this.skills.splice(index, 1);
    },
    handleSubmit() {
      this.passwordError =
        this.password.length > 5
          ? ""
          : "Password must be 6 characters or longer!";
    },
  },
};
</script>

<style>
form {
  max-width: 420px;
  margin: 30px auto;
  background-color: white;
  text-align: left;
  padding: 40px;
  border-radius: 10px;
}
label {
  color: lightslategray;
  display: inline-block;
  margin: 25px 0px 15px;
  font-size: 0.6em;
  letter-spacing: 1px;
  text-transform: uppercase;
  font-weight: bold;
}
input,
select {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
}
input[type="checkbox"] {
  display: inline-block;
  width: 16px;
  margin: 0 10px 0 0;
  position: relative;
  top: 2px;
}
.pill {
  display: inline-block;
  margin: 20px 10px 0 0;
  padding: 6px 12px;
  background: #eee;
  border-radius: 20px;
  font-size: 12px;
  letter-spacing: 1px;
  font-weight: bold;
  color: #777;
  cursor: pointer;
}
button {
  background: #0b6dff;
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  color: white;
  border-radius: 20px;
}
.submit {
  text-align: center;
}
.error {
  color: #ff0062;
  margin-top: 10px;
  font-size: 0.8em;
  font-weight: bold;
}
</style>
