<template>
    <div class="container mt-4">
      <form @submit.prevent="submitForm" class="form-control">
        <!-- Username -->
        <div class="mb-3">
          <label for="username" class="form-label">User Name</label>
          <input
            type="text"
            class="form-control"
            id="username"
            v-model="form.username"
            placeholder="Enter username"
            required
          />
        </div>

          <!-- Password -->
          <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            class="form-control"
            id="password"
            v-model="form.password"
            placeholder="Enter password"
            required
          />
        </div>
  
        <!-- Roles -->
        <div class="mb-3">
          <label class="form-label">Roles</label>
          <div class="form-check" v-for="(role, index) in availableRoles" :key="index">
            <input
              type="checkbox"
              class="form-check-input"
              :id="role"
              :value="role"
              v-model="form.roles"
            />
            <label class="form-check-label" :for="role">{{ role }}</label>
          </div>
        </div>
  
        <!-- Is Active -->
        <div class="mb-3">
          <label class="form-label">Is Active?</label>
          <div class="form-check form-check-inline">
            <input
              class="form-check-input"
              type="radio"
              name="is_active"
              id="isActiveYes"
              value="true"
              v-model="form.active"
            />
            <label class="form-check-label" for="isActiveYes">Yes</label>
          </div>
          <div class="form-check form-check-inline">
            <input
              class="form-check-input"
              type="radio"
              name="is_active"
              id="isActiveNo"
              value="false"
              v-model="form.active"
            />
            <label class="form-check-label" for="isActiveNo">No</label>
          </div>
        </div>
  
        <!-- Timezone -->
        <div class="mb-3">
          <label for="timezone" class="form-label">Select Timezone</label>
          <select class="form-select" id="timezone" v-model="form.preferences.timezone" required>
            <option value="" disabled>Select a timezone</option>
            <option v-for="(timezone, index) in timezones" :key="index" :value="timezone">
              {{ timezone }}
            </option>
          </select>
        </div>
  
        <!-- Submit Button -->
        <button type="submit" class="btn btn-primary w-100">Submit</button>
      </form>
    </div>

</template>
  
<style>
.form-control{
    text-align: left;
}
</style>
  <script>
  export default {
    emits:['emit-data'],
    data() {
      return {
        form: {
          username: "",
          roles: [],
          active: "true", 
          preferences: {
            timezone: "",
          },
          password: "",
        },
        availableRoles: ["admin", "manager", "tester"], 
        timezones: Intl.supportedValuesOf("timeZone"), 
      };
    },
    methods: {
      submitForm() {
        const payload = {
          username: this.form.username,
          roles: this.form.roles,
          active: this.form.active === "true", 
          password: this.form.password,
          preferences: {
            timezone: this.form.preferences.timezone,
          },
        };
  
        this.$emit('emit-data',payload)
        this.resetForm();
      },
      resetForm(){
          this.form = {
          username: "",
          roles: [],
          active: "true", 
          preferences: {
            timezone: "",
          },
          password: "",
        };
      }
    },
  };
  </script>
  