// DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
package client

import (
	"encoding/json"
	"net/http"

	"github.com/zero-os/0-metadata/go/client/goraml"
	"github.com/zero-os/0-metadata/go/client/types"
)

type BdomainService service

// Delete bdomain
func (s *BdomainService) DeleteBdomain(id string, headers, queryParams map[string]interface{}) (*http.Response, error) {
	var err error

	resp, err := s.client.doReqNoBody("DELETE", s.client.BaseURI+"/bdomain/"+id, headers, queryParams)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	return resp, err
}

// Get bdomain, id=int
func (s *BdomainService) GetBdomain(id string, headers, queryParams map[string]interface{}) (types.Bdomain, *http.Response, error) {
	var err error
	var respBody200 types.Bdomain

	resp, err := s.client.doReqNoBody("GET", s.client.BaseURI+"/bdomain/"+id, headers, queryParams)
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

// Update bdomain
func (s *BdomainService) UpdateBdomain(id string, body types.Bdomain, headers, queryParams map[string]interface{}) (types.Bdomain, *http.Response, error) {
	var err error
	var respBody200 types.Bdomain

	resp, err := s.client.doReqWithBody("POST", s.client.BaseURI+"/bdomain/"+id, &body, headers, queryParams)
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

// Get a list of bdomains
func (s *BdomainService) ListBdomain(headers, queryParams map[string]interface{}) ([]types.Bdomain, *http.Response, error) {
	var err error
	var respBody200 []types.Bdomain

	resp, err := s.client.doReqNoBody("GET", s.client.BaseURI+"/bdomain", headers, queryParams)
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