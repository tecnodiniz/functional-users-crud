<template>
    <div class="container mt-4 col-4">
      <form @submit.prevent="submitForm" class="form-control mb-4">
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
        <div class="mb-3 flex-c">
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
        <v-btn type="submit" @click="dialog = true">
          Update
        </v-btn>
      </form>

      <router-link :to="`/`">
          <v-btn
            color="primary mb-4"
          >
            Go Back
          </v-btn>
      </router-link>
    </div>

    <div class="text-center pa-4">

    <v-dialog
      v-model="dialog"
      width="auto"
    >
        <v-card
          max-width="400"
          prepend-icon="mdi-update"
          text="Are you sure?"
          title="Confirm changes"
        >
          <template v-slot:actions>
            <v-btn
              class="ms-auto"
              text="Confirm"
              @click="OpenDialog"
            ></v-btn>

            <v-btn
              class="ms-auto"
              text="Cancel"
              @click="dialog = false"
            ></v-btn>
          </template>
        </v-card>
    
    </v-dialog>

    <v-dialog
      v-model="dialog2"
      width="auto"
    >
        <v-card
          max-width="400"
          prepend-icon="mdi-update"
          text="User Successfully updated"
          title="User Updated"
        >
          <template v-slot:actions>
            <v-btn
              class="ms-auto"
              text="Ok"
              @click="dialog2 = false"
            ></v-btn>
          </template>
        </v-card>
    
    </v-dialog>

  </div>

<!--  
    <v-overlay class="align-center justify-center" v-model="overlay" >
        <div class="card">
            <div class="card-header">
                Confirm Update
            </div>
            <div class="card-body">
                <h5 class="card-title">Are you sure?</h5>
            <div class="flex">
                <button class="btn btn-primary" @click="upadteUser">Yes</button>
                <button class="btn btn-primary" @click="this.overlay = false">No</button>
            </div>
            
            </div>
        </div>
    </v-overlay> -->
  </template>
  
<style scoped>
.flex{
    display: flex;
    justify-content: space-between;
}
.flex-c{
  display: flex;
  flex-direction: column;
}
.form-control{
    text-align: left;
}
</style>
  <script>
import { get_user, update_user } from '@/services/api';

  export default {
    emits:['emit-data'],
    props:{
        id:{
            type: String,
            required: true
        }
    },
    data() {
      return {
        dialog:false,
        dialog2: false,
        overlay: false,
        payload:{},
        form: {
          username: "",
          roles: [],
          active: "true", // Será convertido para booleano no envio
          preferences: {
            timezone: "",
          },
          password: "",
        },
        availableRoles: ["admin", "manager", "tester"], // Papéis disponíveis
        timezones: Intl.supportedValuesOf("timeZone"), // Lista de timezones disponíveis
      };
    },
    created(){
        this.getUser();
    },
    methods: {
      OpenDialog(){
        this.upadteUser()
        this.dialog = false
        this.dialog2 = true
        
      },
      submitForm() {
        const payload = {
          username: this.form.username,
          roles: this.form.roles,
          active: this.form.active === "true", // Converte string para boolean
          password: this.form.password,
          preferences: {
            timezone: this.form.preferences.timezone,
          },
        };
        this.payload = payload;
        this.overlay = true
      },
      upadteUser(){
        update_user(this.id, this.payload)
            .then((response) => {
                console.log('User Successfully updated:', response.data);
                this.getUser()
            })
            .catch((error) => {
                console.error('error:', error);
            });
        
      },
      getUser(){
        get_user(this.id).then((response) =>{
                this.form.username = response.data["user"].username
                this.form.roles = response.data["user"].roles
                this.form.active = response.data["user"].active
                this.form.password = response.data["user"].password
                this.form.preferences.timezone = response.data["user"].preferences.timezone
            })

      }
    },
  };
  </script>
  