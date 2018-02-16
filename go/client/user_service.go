// DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
package client

import (
	"encoding/json"
	"net/http"

	"github.com/zero-os/0-metadata/go/client/goraml"
	"github.com/zero-os/0-metadata/go/client/types"
)

type UserService service

// Delete user
func (s *UserService) DeleteUser(id string, headers, queryParams map[string]interface{}) (*http.Response, error) {
	var err error

	resp, err := s.client.doReqNoBody("DELETE", s.client.BaseURI+"/user/"+id, headers, queryParams)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	return resp, err
}

// Get user, id=int
func (s *UserService) GetUser(id string, headers, queryParams map[string]interface{}) (types.User, *http.Response, error) {
	var err error
	var respBody200 types.User

	resp, err := s.client.doReqNoBody("GET", s.client.BaseURI+"/user/"+id, headers, queryParams)
	if err != nil {
		return respBody200, nil, err
	}
	defer resp.Body.Close()

	switch resp.StatusCode {
	case 200:
		err = json.NewDecoder(resp.Body).Decode(&respBody200)
	default:
		err = goraml.NewAPIError(resp, nil)
	}

	return respBody200, resp, err
}

// Update user
func (s *UserService) UpdateUser(id string, body types.User, headers, queryParams map[string]interface{}) (types.User, *http.Response, error) {
	var err error
	var respBody200 types.User

	resp, err := s.client.doReqWithBody("POST", s.client.BaseURI+"/user/"+id, &body, headers, queryParams)
	if err != nil {
		return respBody200, nil, err
	}
	defer resp.Body.Close()

	switch resp.StatusCode {
	case 200:
		err = json.NewDecoder(resp.Body).Decode(&respBody200)
	default:
		err = goraml.NewAPIError(resp, nil)
	}

	return respBody200, resp, err
}

// Get a list of users
func (s *UserService) ListUser(headers, queryParams map[string]interface{}) ([]types.User, *http.Response, error) {
	var err error
	var respBody200 []types.User

	resp, err := s.client.doReqNoBody("GET", s.client.BaseURI+"/user", headers, queryParams)
	if err != nil {
		return respBody200, nil, err
	}
	defer resp.Body.Close()

	switch resp.StatusCode {
	case 200:
		err = json.NewDecoder(resp.Body).Decode(&respBody200)
	default:
		err = goraml.NewAPIError(resp, nil)
	}

	return respBody200, resp, err
}
